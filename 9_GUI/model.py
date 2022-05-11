import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as mpl
import tkinter
import agentframework
import csv
import os
import random
import matplotlib.animation
import requests
import bs4


'''Set up directories for correct input + output file locations'''
main = os.getcwd()
print (main)
inputs = os.path.join('.', 'input')
print ("Input files are located " + inputs)
outputs = os.path.join('.', 'output')
print ("Output files are located " + outputs)


'''Set up parameters'''
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
environment = []
agents = []
carry_on = True
fig = mpl.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

'''Set up environment'''
file = os.path.join(inputs, 'in.txt')
with open (file, newline='') as q0:
    dataset = csv.reader(q0, quoting=csv.QUOTE_NONNUMERIC)
    for row in dataset:
        rowlist = []
        for value in row:
            rowlist.append(float(value))
        environment.append(rowlist)

'''Make the agents from url'''
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, y, x))



'''Make agents act'''
def update(frame_number):
    '''Define update function, updates the animation
    Args:
        frame_number: iteration number based on generator function (gen_function)
    '''
    global carry_on
    fig.clear()
    if (carry_on):
        random.shuffle(agents)
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
            agents[i].eat_hunger()
        '''Stop processs if agents gain more than 50 in store'''
        half_full_agent_count = 0
        for i in range(num_of_agents):
            if (agents[i].store > 50):
                half_full_agent_count += 1
            if (half_full_agent_count == num_of_agents):
                carry_on = False



    '''plot environment'''
    mpl.xlim(0, 99)
    mpl.ylim(0, 99)
    mpl.imshow(environment)

    '''plot agents'''
    for i in range(num_of_agents):
        mpl.scatter(agents[i]._x,agents[i]._y, color = "black")


'''Define generator function + print reason for process ending'''
def gen_function(b = [0]):
    '''Define gen_function, generator function for ending the animation and printing reason for process ending

    '''
    a = 0
    global carry_on
    while  (a < num_of_iterations) & (carry_on):
        yield a                     #: Returns control and waits next call.
        a = a + 1
    if not carry_on:
        print("Stopping..." + " storage capacity reached.")
    else:
        print("Max iterations met.")
    print("Number of iterations: ", a)


'''Write to output output_env.csv file for environment data'''
file = os.path.join(outputs, 'output_env.csv')
with open(file, 'w', newline='') as q1:
    writer = csv.writer(q1, delimiter=' ')
    for row in environment:
        writer.writerow(row)
print("Environment data is located in " + file)

'''Append data for total stored to total_stored.txt'''
total = 0
for a in agents:
    total += a.store
print("total ", total)
file = os.path.join(outputs, 'total_stored.txt')
with open(file, 'a') as q2:
    q2.write(str(total) + "\n")
    q2.flush
q2.close
print("Stored data is located in " + file)

'''Run animation'''
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=gen_function)
    canvas.draw()


'''Set up GUI'''
root = tkinter.Tk() # Main window.
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)
tkinter.mainloop()
