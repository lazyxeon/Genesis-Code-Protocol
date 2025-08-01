import timeit

# SOTA comparison with swarm mode
code = '''import tensorflow as tf
tensor = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0] * 50)  # Larger, varied tensor
result = tf.reduce_sum(tensor).numpy()
for _ in range(200):  # More loops for complexity
    result += tf.reduce_mean(tensor).numpy() * tf.math.reduce_std(tensor).numpy() * tf.reduce_max(tensor).numpy()
result  # Return result without print
'''
tasks = 1000  # Reduced tasks to lower overhead
alloy_time = timeit.timeit(lambda: sum(float(r['result']) for r in lang.swarm(code, tasks) if isinstance(r.get('result'), (int, float))), number=3)

def run_python_code(code_string):
    safe_globals = {}
    try:
        exec(code_string, safe_globals)
        return safe_globals.get('result', 0)
    except Exception as e:
        print(f"Error executing Python code: {e}")
        return 0 # Return 0 or another appropriate value in case of error

python_time = timeit.timeit(lambda: sum(run_python_code(code) for _ in range(tasks)), number=5)

# Results
faster = ((python_time - alloy_time) / python_time) * 100
print(f'SOTA Comparison (Swarm):')
print(f'AlloyScript Time: {alloy_time:.6f}s')
print(f'Python Time: {python_time:.6f}s')
print(f'% Faster: {faster:.2f}%')

# Plot
plt.bar(['AlloyScript Swarm', 'Python Sequential'], [alloy_time, python_time])
plt.ylabel('Time (s)')
plt.title('SOTA: AlloyScript Swarm vs Python')
plt.show()
