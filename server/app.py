#!/usr/bin/env python3
from flask import Flask, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask import Flask, jsonify


from models import db, Newsletter

@@ -79,6 +81,45 @@ def get(self, id):
        )

        return response

    def patch(self, id):

        record = Newsletter.query.filter_by(id=id).first()

#Looping through the form data gives us its keys, the attribute names to be changed        
        for attr in request.form:

#we can set each attribute on the Newsletter object to its new value with setattr()            
            setattr(record, attr, request.form[attr])

            db.session.add(record)
            db.session.commit()

            response_dict = record.to_dict()

            response = make_response(
                jsonify(response_dict),
                200
            )

            return response


    def delete(self, id):

        record = Newsletter.query.filter_by(id=id).first()

        db.session.delete(record)
        db.session.commit()

        response_dict = {"message": "record successfully deleted"}

        response = make_response(
            jsonify(response_dict),
            200
        )

        return response

api.add_resource(NewsletterByID, '/newsletters/<int:id>')
