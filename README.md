# AutoML Benchmarking

To run a benchmark call the `benchmark.py` file with three arguments:

1. The AutoML framework that should be evaluated, see [frameworks.json](resources/frameworks.json) for supported frameworks. If you want to add a framework see [here](docker/readme.md).
2. The benchmark suite to run. Should be one implemented in [benchmarks.json](resources/benchmarks.json)
3. If the benchmark should be run `local` or on `aws`.
4. (Optional) a file to append the results to


## Installation

To run the benchmarks, you will need [Docker](https://docs.docker.com/install/), Python 2 or 3, and the `boto3` Python package.


## Generate Docker Images

The first time you run the benchmarks, you will need to generate the Docker images. As an example, if you want to run the Random Forest benchmark, you would first need to execute the following to generate the Random Forest Docker image:

```
cd docker
./generate_docker.sh RandomForest  # Directory name from docker folder
```
This will generate the Docker image for the Random Forest benchmark, where "RandomForest" is the folder name inside the `./docker` folder.


## Run the benchmark locally

A minimal example would be to run the test benchmarks with a random forest:

```
python benchmark.py RandomForest test local
```
The first time you execute the benchmark, it will download all the dependencies to install in the Docker image, so that will take some time.

The script will produce output that records the OpenML Task ID, the fold index the result.  The result is the score on the test set, where the score is a specific model performance metric (e.g. "AUC") defined by the benchmark.

```
  benchmark_id  fold    result
0       test_1     0  0.933333
1       test_1     1  1.000000
2       test_2     0  0.811321
3       test_2     1  0.849057
```


## Run the benchmark on AWS

To run a benchmark on AWS you additionally need to

- Have `boto3` set up on you machine with access to your AWS account
- Change the name of the `ssh_key` and `sec_group` to values associated with you AWS account.

```
python benchmark.py randomForest test aws
```

The output shows the instances starting, outputs the progress and then the results for each dataset/fold combination:

```
Created 4 jobs
Starting instances
Instance pending
Instance pending
Instance pending
Instance pending
Instance pending
0/4 jobs done
0/4 jobs done
0/4 jobs done
0/4 jobs done
0/4 jobs done
0/4 jobs done
0/4 jobs done
0/4 jobs done
0/4 jobs done
0/4 jobs done
1/4 jobs done
1/4 jobs done
1/4 jobs done
1/4 jobs done
1/4 jobs done
1/4 jobs done
2/4 jobs done
4/4 jobs done
All jobs done!
Terminating Instances:
Termination successful
Termination successful
Termination successful
Termination successful

  benchmark_id  fold              result
0       test_1     0  0.9333333333333333
1       test_1     1                 1.0
2       test_2     0  0.8679245283018868
3       test_2     1  0.8490566037735849

```