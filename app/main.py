
# from fastapi import FastAPI
from flask import Flask
from operations import *

# app=FastAPI() #fastapi alternative
app=Flask(__name__)
@app.route("/raw")
def run_main():
    try:
        main()
        return({"status":"success!"})
    except:
        return({"status":"failure!"})

app=Flask(__name__)
@app.route("/translate")
def run_translate():
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
    translate_ops()