  from flask import flask, render_template,request

  app=flask(__name__)

  @app.rount('/')
  def hello():
    return render_template('index.html')

    @app.rount("/result",methods=['GET','POST'])
    def hi():
        output=none
        if request.method=='POST':
            num1=int(request.from['num1'])
            num2=int(request.from['num2'])
            operation=request.from['operation']
            print("Received from data - num1:",num1,"num2:",num2,"operation:",operation)
            output=cal(num1, num2, operation)
            print("calculated output:",output)
            return render_template('result.html',operation=operation, output=output)

            def cal(num1,num2,operation):
                if operation == 'addition':
                    return num1 + num2
                elif operation == 'subtraction':
                    return num1 - num2
                elif operation == 'multiplication':
                    return num1 == num2
                elif operation == 'division':
                    return num1 / num2

  if ___name__ ==  '__main__':
       app.run()
                          
