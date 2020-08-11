import json
from flask import Flask, request
from helpers import queries

app = Flask(__name__)

dummy = {
	"ok": 'true',
	"members": [{
			"id": "W012A3CDE",
			"real_name": "Egon Spengler",
			"tz": "America/Los_Angeles",
			"activity_periods": [{
					"start_time": "Feb 1 2020  1:33PM",
					"end_time": "Feb 1 2020 1:54PM"
				},
				{
					"start_time": "Mar 1 2020  11:11AM",
					"end_time": "Mar 1 2020 2:00PM"
				},
				{
					"start_time": "Mar 16 2020  5:33PM",
					"end_time": "Mar 16 2020 8:02PM"
				}
			]
		},
		{
			"id": "W07QCRPA4",
			"real_name": "Glinda Southgood",
			"tz": "Asia/Kolkata",
			"activity_periods": [{
					"start_time": "Feb 1 2020  1:33PM",
					"end_time": "Feb 1 2020 1:54PM"
				},
				{
					"start_time": "Mar 1 2020  11:11AM",
					"end_time": "Mar 1 2020 2:00PM"
				},
				{
					"start_time": "Mar 16 2020  5:33PM",
					"end_time": "Mar 16 2020 8:02PM"
				}
			]
		}
	]
}

@app.route('/get-users', methods=['GET', 'POST'])
def fetchAllData():
	id = request.args['id']
	print(id)
	if(id):
		resp = queries.get_member_details(id)
		print(resp)
		return resp
	else:
		return {"Please enter the id correctly to get all the details"}
	return {'Network Error'}


@app.route('/add-member', methods=['GET','POST'])
def insertMember():
	try:
		id = request.args['id'] 
		real_name = request.args['real_name'] 
		tz = request.args['tz']

		if(id and real_name and tz):
			resp = queries.insert_member(id, real_name, tz)
			return {"statusCode": 200, 'response': resp}
		else:
			return {'response': 'please insert unique id, real_name , tz'}
	except:
		return {'Network Error'}
	
    

@app.route('/add-member-activity', methods=['GET','POST'])
def insertMemberACtivity():
	try:
		id = request.args['id'] 
		start_time = request.args['start_time'] 
		end_time = request.args['end_time']
		if(id and start_time and end_time):
			resp = queries.insert_member_activity(id, start_time, end_time)
			return {"statusCode": 200, 'response': resp}
		else:
			return {'response': 'please all datas , i.e., id, start_time, end_time'}
	except:
		return {'Network error'}


@app.route('/dummy', methods=['GET'])
def getDummyData():
    return dummy
