import threading
from flask import Flask, request
import asyncio
import nest_asyncio
nest_asyncio.apply() #required for nested threading in flask

print(f"Global thread is: {threading.current_thread().name}")
app = Flask(__name__)

# Example use of threading with asyncio module and threading library (for documenting threads)
@app.route('/', methods=['GET'])
async def thread_test():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    result_1 = loop.run_until_complete(wait(3))
    result_2 = loop.run_until_complete(wait(6))
    result_3 = loop.run_until_complete(wait(9))

    return '<br>'.join([result_1, result_2, result_3]) #return threading results on webpage separated by newlines

async def wait(wait_time):
    await asyncio.sleep(wait_time)
    result = f"Completed loop for {wait_time} seconds in thread: {threading.current_thread().name}"
    print(result)
    return result

# Example use of flask API endpoint and small calculation in python, based on https://pubmed.ncbi.nlm.nih.gov/18184978/
@app.route('/optimal_height_calc', methods=['GET', 'POST'])
def leg_length_calc():
    length = request.args.get('lower_leg_length')
    return f"Optimal bed height for {length} cm lower leg length is: {str(float(length) * 1.2)} cm"




