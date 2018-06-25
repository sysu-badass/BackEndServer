class DaoHelper:
    @staticmethod
    def update(obj, key, value):
        if (hasattr(obj, key)):
            setattr(obj, key, value)
    
    @staticmethod
    def delete(db, obj):
        if (obj):
            db.session.delete(obj)
    
    @staticmethod
    def commit(db):
        flag = True
        try:
            db.session.commit()
        except:
            db.session.rollback()
            flag = False
        return flag
    
    # @staticmethod
    # def add_comit(db, obj):
    #     flag = True
    #     try:
    #         db.session.add(obj)
    #         db.session.commit()
    #     except:
    #         db.session.rollback()
    #         flag = False
    #     return flag

    # @staticmethod
    # def update_commit(db, obj, key, value):
    #     flag = True
    #     if (hasattr(obj, key)):
    #         setattr(obj, key, value)
    #         try:
    #             db.session.commit()
    #         except:
    #             db.session.rollback()
    #             flag = False
    #     else:
    #         flag = False
    #     return flag

    # @staticmethod
    # def del_commit(db, obj):
    #     flag = True
    #     if (obj):
    #         db.session.delete(obj)
    #         db.session.commit()
    #     else:
    #         flag = False
    #     return flag