
# from fastapi import FastAPI
from flask import Flask
from operations import *

# app=FastAPI() #fastapi alternative
app=Flask(__name__)
@app.route("/raw")
def root():
    try:
        main()
        return({"status":"success!"})
    except:
        return({"status":"failure!"})

app=Flask(__name__)
@app.route("/translate")
def root():
    try:
        translate_ops()
        return({"status":"success!"})
    except:
        return({"status":"failure!"})

if __name__=='__main__':
    # try:
    #     main()
    #     print({"status":"success!"})
    # except:
    #     print({"status":"failure!"})
    main()