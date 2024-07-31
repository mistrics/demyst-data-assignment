# Solutions

## Problem 1

Run docker build and docker run to test the solution. <BR><BR>
`cd solution1`<BR>
`docker build -t solution1 .` <BR>
`docker run -v $(pwd):/app solution1`
output.csv will be generated inside folder.

## Problem 2

Run docker build and docker run to test the solution. <BR><BR>
`cd solution2`<BR>
`docker build . -t solution2.1 -f Dockerfile.Python`<BR>
`docker run -v $(pwd):/app solution2.1`<BR>
Above commands will create a test_data.csv file. Currently its generating 100 records, but that number can be increased to load test the system for 2GB.

`docker build . -t solution2.2 -f Dockerfile.Spark` <BR>
`docker run -v $(pwd):/app -p 4040:4040 solution2.2`<BR>
Open http://localhost:4040 for Spark UI
Once complete, there will be a anonymized_data.csv folder with csv data file in it.
