Resource Constraint Project Scheduling Problem
A company has a small project consisting of multiple varying small task. Each task requires certain types of resource. A list of all resource with their availability timeframe are to help make the grogress in the project.

The program takes an excel file as the input and produces a gantt chart of task, task and resource calendar.

Detailed Descriptions
Tasks' key features
Resource Requirement: in the current scope of the project, this attribute refers to the list of qualities that personnel carries out this task must satisfies
Task Predecessors: list of all other tasks must be done before this task is finished
Task duration: the length (in hours of the tasks)
Resource's key features
Qualities: list of all qualities that a resource possesses, if this Qualities satisfies Task Resource Requirement, this resource may be used for this task

Cost: Cost for a resource are calculated based on the qualities that resource possesses

Timeframe's key attribute
Type: can be one of ["Morning Shift","Afternoon Shift","Overtime", "Rest time"], each types also defines the cost of using a resource within this Timeframe

An availability list of all resources: list of all avalable resources at this Timeframe

How to Run
Prepare your excel file in the same format as the file in "data/input"

Rename your excel file to "Data.xlsx"

Activate Python Virtual Environment and run following command:

python main.py

All the results are stored in "data/output" folder

Ongoing Work
A GUI is being implemented for easy usage More versions of algorithms are being added