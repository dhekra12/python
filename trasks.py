tasks= input("Enter your tasks for today separted by a comma: ").split(", ")
done_tasks =[]
ongoing_tasks=[]
for task in tasks:
    print(f"\n {task}  \n")
    done= input(f"did you finished the {task} \n")
    if done == "yes":
        print("Nice job")
        done_tasks.append(task)
    else:
        print("try not to put it off")
        ongoing_tasks.append(task)
    print("---------------------")
progress= input("Do you want to see your today's progress?(yes/ no) \n")
if progress == "yes":
  print("""
        ***** Done Tasks ***** 
        """)
  print(done_tasks)
  print("""
        ***** Ongoing Tasks ***** 
        """)
  print(ongoing_tasks)
else:
    print("Press enter to Exite")
        


        
    
     