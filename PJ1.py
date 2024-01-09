import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict, deque
import datetime as dt
# <--- Đọc dữ liệu sheet Task --->
def read_Task(excel_file_path):
    # Đọc dữ liệu Task 
    task_df = pd.read_excel(excel_file_path, sheet_name='Task', nrows=41)

    # Đọc dữ liệu từng cột sheet Task
    task_id_list = task_df['ID'].tolist()
    task_name_list = task_df['Name'].tolist()
    task_group_list = task_df['Group'].tolist()
    task_predecessors_list = task_df['Predecessors'].tolist()
    task_duration_list = task_df['Duration'].tolist()
    task_resource_requirement_list = task_df['Resource Requirement'].tolist()
    
    pre_list = []
    for predecessor in task_predecessors_list:
        if isinstance(predecessor, str):
            parts = predecessor.split(";")
            pre_list.append(parts)
        else: 
            pre_list.append([])
    # print(pre_list)

    resource_require_list = dict()
    for index, row in task_df.iterrows():
        id = int (row['ID'])
        resource_require_list[id] = dict()

        task = row['Resource Requirement']
        idx = task.find(':')
        if idx != -1:
            role = task[:idx].strip()
            resource_require_list[id]['role'] = role
            resource_require_list[id]['skill'] = dict()
            for text in task [idx + 1:].split(','):
                skill, num = text.strip().split(':')
                skill = skill.strip()
                num = int(num.strip())
                resource_require_list[id]['skill'][skill] = num
    # print(resource_require_list)

    return task_id_list, task_name_list, pre_list, task_duration_list, resource_require_list # Chỉ trả về cần thiết cho sắp xếp topological

# <--- Đọc dữ liệu sheet Resource --->
def read_Resources(excel_file_path):
    #Đọc dữ liệu Resource
    resource_df = pd.read_excel(excel_file_path, sheet_name = 'Resources', nrows = 20)

    #Đọc dữ liệu từng cột sheet Resources
    resource_id_list = resource_df['ID'].tolist()
    resource_type_list = resource_df['Type'].tolist()
    resource_description_list = resource_df['Description'].tolist()
    resource_qualities_list = resource_df['Qualities'].tolist()
    resource_skill_groups_list = resource_df['Skill Groups'].tolist()
    resource_cost_list = resource_df['Cost'].tolist()

    qualities_list = dict()
    for index, row in resource_df.iterrows():
        id = int (row['ID'])
        qualities_list[id] = dict()

        resource = row['Qualities']
        idx = row['Type']
        qualities_list[id]['Type'] = idx
        qualities_list[id]['skill'] = dict()
        for text in resource.split(','):
            skill, num = text.strip().split(':')
            skill = skill.strip()
            num = int(num.strip())
            qualities_list[id]['skill'][skill] = num

    # print(qualities_list)

    return resource_id_list, resource_type_list, resource_description_list, qualities_list, resource_skill_groups_list, resource_cost_list

def read_Timeframe(excel_file_path):
    #Đọc dữ liệu Timeframe
    timefr_df = pd.read_excel(excel_file_path, sheet_name = 'Timeframe')

    #Đọc dữ liệu từng cột Sheet Timeframe
    timeframe_start_list = timefr_df['start'].tolist()
    timeframe_end_list = timefr_df['end'].tolist()
    timeframe_type_list = timefr_df['type'].tolist()
    timeframe_statement_list = []
    for i in range(1,21):
        id_str = "ID_" + str(i)
        timeframe_statement_list.append(timefr_df[id_str].tolist())
    
    #Chuẩn hóa dữ liệu về dạng datetime
    time_start = []
    time_end = []
    for i in timeframe_start_list:
        time_start.append(i.to_pydatetime())
    for i in timeframe_end_list:
        time_end.append(i.to_pydatetime())
    # print(timeframe_statement_list)
    return time_start, time_end, timeframe_type_list, timeframe_statement_list

# <--- Các hàm Topological Sort --->
    
def topological_sort(graph):
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    queue = deque([node for node in in_degree if in_degree[node] == 0])
    result = []

    while queue:
        current_node = queue.popleft()
        result.append(current_node)

        for neighbor in graph[current_node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check for cycles
    if len(result) != len(graph):
        print("The graph has cycles. Topological sort not possible.")
        return None
    else:
        return result

# <--- Hàm vẽ biểu đồ --->
def draw_graph(adj, task_name_list):
    G = nx.DiGraph()

    for i in range(len(adj)):
        for j in adj[i]:
            G.add_edge(task_name_list[i], task_name_list[j-1])

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=8, font_color="black", font_weight="bold", edge_color="gray", arrowsize=10)
    plt.title("Biểu đồ công việc")
    plt.show()

# solve

# def calc_timeframe(lis):
#     if len(lis) == 1:
#         task_id = lis[0]
#         finished_task = False
#         while duration_list[task_id - 1] > 0:
#             if duration_list[task_id - 1] >= 4:
#                 finished_task = True
#                 duration_list[task_id - 1] = 4 - duration_list[task_id - 1]
#             else: 
#                 duration_list[task_id - 1] -= 4
#             result.append([task_id,assigned_resources[task_id],duration_list[task_id - 1]])

#     pass
# <--- Xếp lịch công việc --->
def main():
    excel_file_path = 'Data.xlsx'

    # Đọc dữ liệu từ sheet Task
    id_col, name_col, pre_list, duration_list, resource_require_list= read_Task(excel_file_path)
    
    # Đọc dữ liệu từ sheet Resources
    rs_id, re_type, rs_des, rs_qualities, rs_skgroups, rs_cost = read_Resources(excel_file_path)

    # Đọc dữ liệu từ sheet Timeframe (bạn có thể thêm logic xử lý thời gian ở đây nếu cần)
    tf_start, tf_end, tf_type, tf_statement = read_Timeframe(excel_file_path)
    

    # Task NoV (number of vertices) = true task + 1
    NoV = len(id_col) + 1
    adj = [[] for _ in range(NoV)]
    pre_task_list = [[] for _ in range(NoV)]
    for i in range(len(id_col)):
        task_id = id_col[i]
        task_pre = pre_list[i]
        for pre in task_pre:
            adj[int(pre[:-2])].append(task_id)
            pre_task_list[task_id].append(int(pre[:-2]))
    list_adj = {}
    for i in range(len(adj)):
        list_adj[i] = adj[i]
    for i in pre_task_list:
        print(i)
    # Sắp xếp topological
    
    task_sorted_order = topological_sort(list_adj)
    task_sorted_order.remove(0)
    # Tạo một danh sách để lưu trữ người thực hiện cho mỗi công việc
    assigned_resources = [] # contains: task_id, resource_id, resource_cost, task_duration

    # Duyệt qua danh sách công việc đã sắp xếp topological
    assign_active = [False] * 42
    task_condition = [True] * 42
    for task_id in task_sorted_order:

        task_name = name_col[task_id-1]
        task_requirements = resource_require_list[task_id]

        # Tìm người thích hợp cho công việc
        suitable_resources = dict()
        for i in rs_qualities:
            if rs_qualities[i]['Type'] == task_requirements['role']:
                res_qualities = rs_qualities[i]['skill']
                task_req = task_requirements['skill']
                cnt = 0
                for key in task_req:
                    if res_qualities[key] >= task_req[key]:
                        cnt += 1
                if cnt == len(task_req) and task_condition[task_id]:
                    assign_active[task_id] = True
                    suitable_resources[task_id] = i
        if not assign_active[task_id]:
            for j in adj[task_id]:
                task_condition[j] = False
            
        # Nếu có nhiều người phù hợp, chọn người có cost bé nhất
        if len(suitable_resources) > 0:
        #     sorted_resources = sorted(suitable_resources, key=lambda element : element[1])
            assigned_resources.append(suitable_resources)
    # print(assigned_resources)

    # Sử lí dữ liệu Timeframe
    # Viết dữ liệu mới lên file timeframe
    # timeframe_execl_path = 'Timeframe.xlsx'
    # data_timeframe = dict()
    # data_timeframe['start'] = tf_start
    # data_timeframe['end'] = tf_end
    # data_timeframe['type'] = tf_type
    # note_list = []
    # data_timeframe['note'] = note_list
    
    # taskID, taskName, resorceID, start, end

    
        
    
#   # In ra danh sách cụ thể
    # print("Danh sách công việc và người thực hiện:")
    # for task_id, resource_id in assigned_resources.items():
    #     print(f"ID_Task: {task_id}, ID_Resource: {resource_id}")

    # #In ra danh sách công việc sau khi sắp xếp topological
    # print("Danh sách công việc sau khi sắp xếp topological:")
    # for task_id in (task_sorted_order):
    #     print(f"ID: {task_id}, Tên: {name_col[task_id-1]}")

    # draw_graph(adj, name_col)
    # plt.savefig('task_graph.png')
    # plt.show()
    
if __name__ == "__main__":
    # Gọi hàm main khi chạy chương trình
    main()


