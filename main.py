from website import create_app

app = create_app()

#only if we run this file, not import ,are we going to execute the second line
if __name__ == '__main__':  # I dont want to run it if the __name__ is not equal to main

#debug = true means it will automatically add the new line of codes and checks it's functionality
    app.run(debug=True)
    
    


