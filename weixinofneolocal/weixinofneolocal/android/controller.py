#coding=utf-8
from .xml_api import  *
from app.models import  *
import json
from django.db.models import Q 

def get_me(name):
    me =  (User.objects.filter(username=name))[0].userprofile;
    json_data = me_json(me,0);
    return json_data;

def get_userprofile(name):
    json_data = None;
    userinfo  = (User.objects.filter(username=name))[0];
    profile =  userinfo.userprofile;
    signature = profile.getSignature();
    photos = profile.pic_set.all();
    json_data = profile_reply_json(userinfo,profile,signature,photos);
    return json_data;

def get_userstatus(name):
    json_data = None;
    status =  (User.objects.filter(username=name))[0].userprofile.statu_set.all()
    json_data = status_reply_json(status);
    return json_data;

def get_userfriend(name):
    relation =  (User.objects.filter(username=name))[0].userprofile.getFriendsSet();
    json_data = friend_reply_json(relation,1);
    return json_data;

def get_nearby(name):
    relation =  (User.objects.filter(username=name))[0].userprofile.getNearBy();
    json_data = friend_reply_json(relation,0);
    return json_data;

def create_user(data,pic='android/headimg/default_head_185x185.jpg'):
    rtn = True;
    user = User.objects.filter(username=data["username"]);
    if  len(user)==0:
        user = User.objects.create_user(username=data["username"],first_name=data["first_name"],
                                        last_name=data["last_name"], email=data["email"], 
                                        password=data["password"])
        user.is_staff = int(data["is_staff"]);
        user.is_active = int(data["is_active"]);
        user.save();
        
        profile = UserProfile(user=user,gender=int(data["gender"]),headimg=pic,
                              birthday=data["birthday"],constellation=data["constellation"],
                                phone=data["phone"],vip=int(data["vip"]),grouprole=int(data["grouprole"]),
                                  industry=data["industry"],device=int(data["device"]),
                                multipic=int(data["multipic"]))
        profile.save();
        rtn =True;
    else:
        rtn = False;
    
    return rtn;
    
def update_user(data):
    rtn = True;
    user = User.objects.filter(username=data["username"]);
    if  len(user)==0:
        user = User.objects.create_user(username=data["username"],first_name=data["first_name"],
                                        last_name=data["last_name"],  email=data["email"], 
                                        password=data["password"])
        rtn =True;
        user.is_staff = int(data["is_staff"]);
        user.is_active = int(data["is_active"]);
    else:
        user.first_name=data["first_name"];
        user.last_name=data["last_name"];
        user.email=data["email"];
        user.is_staff=int(data["is_staff"]);
        user.is_active=int(data["is_active"]);
        rtn = False;
    user.save();
    return rtn;

def set_pwd(data):
    user = User.objects.filter(username=data["username"]);
    if  len(user)!=0:
        user.set_password(data["password"]);
        user.save();

def set_userprofile(data, pic='android/headimg/default_head_185x185.jpg'):
    user = User.objects.filter(username=data["username"])
    if len(user)!=0:
        profile = user[0].userprofile;
        profile.gender = int(data["gender"]);
        profile.headimg = pic;
        profile.birthday = data["birthday"];
        profile.constellation = data["constellation"];
        profile.phone = data["phone"];
        profile.vip = int(data["vip"]);
        profile.grouprole = int(data["grouprole"]);
        profile.industry = data["industry"];
        profile.device = int(data["device"]);
        profile.multipic = int(data["multipic"]);
        profile.save();
    
def update_headpic(name,pic):
    users = User.objects.filter(username=name)
    if len(users)!=0:
        profile = users[0].userprofile;
        profile.headimg = pic;
        profile.save();
        return True;
    return False;
    
def set_relation(json_data):
    data = json.loads(json_data);
    user = User.objects.filter(id=int(data["userid"]));
    relate = UserRelation.objects.filter(userid = int(data["userid"])).filter (frendid = int(data["frendid"]));
    if len(user)!=0 and len(relate)==0:
        relation = UserRelation.objects.create(name = data["name"],userid = int(data["userid"]),frendid = int(data["frendid"]),
                                          relation=int(data["relation"]),profile=user[0].userprofile);
        relation.save();
    
def set_status(json_data,pic):
    data = json.loads(json_data);
    user = User.objects.filter(id=int(data["userid"]));
    if len(user)!=0:
        status = UserStatus.objects.create(name = data["name"],userid = int(data["userid"]),content = data["content"],
                                          content_img=pic,content_count =  int(data["content_count"]),
                                          location=user[0].userprofile.getlocation(),profile=user[0].userprofile);
        status.save();
    
    
def set_signature(json_data, pic):
    data = json.loads(json_data);
    user = User.objects.filter(id=int(data["userid"]));
    if len(user)!=0:
        signature = UserSignature.objects.create(name = data["name"],userid = int(data["userid"]),sign = data["sign"],
                                          sign_pic = pic,profile=user[0].userprofile);
        signature.save();
    
def set_location(json_data):
    data = json.loads(json_data);
    user = User.objects.filter(id=int(data["userid"]));
    if len(user)!=0:
        location = UserLocation.objects.create(name = data["name"],userid = int(data["userid"]),latitude = float(data["latitude"]),
                                          longitude = float(data["longitude"]), info = data["info"],profile=user[0].userprofile);
        location.save();
    
def set_userphoto(json_data,pic):
    data = json.loads(json_data);
    user = User.objects.filter(id=int(data["userid"]));
    if len(user)!=0:
        photos = UserPhotos.objects.create(name = data["name"],userid = int(data["userid"]),userphoto = pic,
                                           info = data["info"],profile=user[0].userprofile);
        photos.save();
    
    