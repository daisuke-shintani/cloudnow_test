from sqlalchemy.orm import Session
from . import models, schemas

# タイトル
def get_search(search: str,db: Session, skip: int  =0, limit: int =100):
    service =db.query(models.Cloud).offset(skip).limit(limit).all()
    # return service
    
    i=0
    id_list=[]
    
    for t in service:
        a=service[i].title
        b=service[i].user_name
        c=service[i].cloud_service
        d=service[i].desc
        e=service[i].cloud_id
        i=i+1
        if search in a or search in b or search in c or search in d:
            
            id_list =id_list+[service[e-1].cloud_id]
    
    j=0
    json_list =[]
    for num in id_list:
        json_list += [service[num-1]]
    
    return json_list
        

    
   
    # a=data.cloud_service
    # b=data.user_name
    # c=data.desc
    # d=data.title
    # if search in a or search in b or search in c or search in d:
    #     return "daisuke"
   
# 確認
def get_clouds(db: Session, skip: int  =0, limit: int =100):
    return db.query(models.Cloud).offset(skip).limit(limit).all()

# 登録
def create_cloud(db: Session, cloud: schemas.Cloud):
    # インスタンスの生成
    db_cloud = models.Cloud(
        title =cloud.title,
        cloud_service = cloud.cloud_service,
        user_name =cloud.user_name,
        desc = cloud.desc
    )
    db.add(db_cloud)
    db.commit()
    db.refresh(db_cloud)
    return db_cloud