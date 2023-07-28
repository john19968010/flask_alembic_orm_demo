from flask_apispec import MethodResource, marshal_with, doc, use_kwargs
import util
from . import user_router_model
from model import User, db



####### API Action #########

class Users(MethodResource):
    # GET_ALL
    @doc(description='Get Users info.', tags=['User'])
    @use_kwargs(user_router_model.UserGetSchema, location="query")
    @marshal_with(user_router_model.UsersGetResponse, code=200)
    # @jwt_required()
    def get(self, **kwargs):
        filter_name = kwargs.get("name")
        
        if filter_name:
            users = User.query.filter(User.name.ilike(f"%{filter_name}%")).all()
        else:
            users = User.query.all()

        user_info = [{
            "id": user.id,
            "name": user.name,
            "account": user.account,
            "gender": user.gender,
            "create_at": user.create_at
        } for user in users] 
        return util.success(user_info)

    # POST
    @doc(description='Create User.', tags=['User'])
    @use_kwargs(user_router_model.UserPostSchema, location="form")
    @marshal_with(user_router_model.UserCommonResponse, code=201)
    def post(self, **kwargs):
        user = User(**kwargs)
        db.session.add(user)
        db.session.commit()
        return util.success()




class SingleUser(MethodResource):
    @doc(description='Get Single user info.', tags=['User'])
    @marshal_with(user_router_model.UserGetResponse, code=200)
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        if user is None:
            return util.failure({"message":"User not found"})
        
        user_info = {
            "id": user.id,
            "name": user.name,
            "account": user.account,
            "gender": user.gender,
            "create_at": user.create_at
        }
        
        return util.success(user_info)

    @doc(description='Update User info.', tags=['User'])
    @use_kwargs(user_router_model.UserPatchSchema, location="form")
    @marshal_with(user_router_model.UserCommonResponse, code=201)
    def patch(self, id, **kwargs):
        user_info = User.query.filter_by(id=id).first()
        if user_info is None:
            return util.failure({"message":"User not found"})
        
        kwargs = {k: v for k, v in kwargs.items() if v is not None or v != ""}
        
        User.query.filter(User.id == id).update(kwargs)
        db.session.commit()

        return util.success()

    @doc(description='Delete User info.', tags=['User'])
    @marshal_with(None, code=204)
    def delete(self, id):
        User.query.filter_by(id=id).delete()
    
        db.session.commit()
        return util.success()
        


