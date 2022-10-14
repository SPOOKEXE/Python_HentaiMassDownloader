# https://towardsdatascience.com/advanced-multi-tasking-in-python-applying-and-benchmarking-threadpools-and-processpools-90452e0f7d40

from concurrent import futures as futures

def CompleteThreadTask(parent_function=None, arguments_array=[], worker_count=25) -> list:
	if parent_function == None:
		print("Function must be passed for multi-threading.")
		return None
	if worker_count < 1:
		print("Worker count must be larger than 0 to use multi-threading.")
		return None
	results = []
	with futures.ThreadPoolExecutor(max_workers=worker_count) as executor:
		future_promises = []
		for argument in arguments_array:
			future_promises.append(
				executor.submit(parent_function, argument)
			)
		for future_promise in futures.as_completed(future_promises):
			results.append(future_promise.result())
	return results

if __name__ == '__main__':
	import time
	def ExampleFunction(argument : list) -> list:
		print(argument)
		time.sleep(2)
		return ["List", "of", "strings"]

	def StartParse(arg_array):
		print("start parse")
		result = CompleteThreadTask(parent_function=ExampleFunction, arguments_array=arg_array, worker_count=2)
		print("end parse")
		return result

	arg_test = []
	for i in range(1000):
		arg_test.append([i])
	# StartParse(arg_test)

	print(CompleteThreadTask(
		parent_function=StartParse,
		arguments_array=[arg_test, arg_test, arg_test],
		worker_count=50)
	)
