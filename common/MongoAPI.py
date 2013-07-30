#-*- coding:utf-8 -*-

import os

class MongoEye():
    pymongo = __import__('pymongo')
    
    def __init__(self, 
                 mongo_host='192.168.0.116', 
                 mongo_database='esdb', 
                 mongo_port=27017):
        # connect to mongodb
        self.conn = MongoEye.pymongo.MongoClient(host=mongo_host, 
                                               port=mongo_port)

        # go to database
        self.db = self.conn[mongo_database]
        self.collections = self.db.collection_names()
    
    def show_collections(self):
        '''
        Usage:
        e = TheEye(mongo_database='nlp')
        for k, v in e.show_collections().iteritems():
            print k, v
            
        Every database has a collection called 'system.indexes'
        '''
        
        statistics = dict()
        for collection_name in self.collections:
            if collection_name == 'system.indexes': continue
            col = self.db[collection_name]
            statistics.setdefault(collection_name, col.count()) 
            
        self.conn.disconnect()
        
        return statistics

    def get_records(self, collection, find_dic):
        # get collection
        col = self.db[collection]

        # get all unused
        records = col.find(find_dic,timeout=False).sort('_id',1)

        for record in records:
            yield record

    def show_all_possible_keys(self, collection):
        keys = []
        
        records = self.get_records(collection, {})
        for record in records:
            keys.extend(record.keys())

        return set(keys)            
    
    def getId(self,collection):
        o = self.db['counters'].find_and_modify(query= {'_id': collection}, update={'$inc': {'c': 1}})
        return o['c']

    def get_record_return(self,collection,find_dic,get_dic):
        # get collection
        collect = self.db[collection]

        # get all unused
        records = collect.find(find_dic,get_dic,timeout=False)

        for record in records:
            yield record

    #this function changes the value of a key in a dictionary
    def update(self,collection,find_dic, new_record):
        collect = self.db[collection]
        
        # insert into collection
        collect.update(find_dic,{'$set':new_record})
        
    def unset(self, collection, find_dic, rm_record):
        collect = self.db[collection]

        # insert into collection
        collect.update(find_dic,{'$unset':rm_record})

    #this function is to add something new into records relating to some specific "corp_id"
    def push(self, collection, find_dic, push_dic):
        collect = self.db[collection]

        # push the record to one column
        collect.update(find_dic, {'$push': push_dic})

##    def pushToDetail(self, collection, find_dic, key_level1, key_level2, value_level2, update_dic):
##        collect = self.db[collection]
##
##        # db.pc_test.update({_id:0,          'set.url':'www.baidu.com'},         {$push:   {'set.$.minor_id_new':          "3"}},             false, true)
##        # collect.update   ({find_dic,  'key_level1.key_level2':'value_level2'}, {'$push': {'key_level1.$.update_dic_key': update_dic_value}},False, True) 
##        #                     find_detail,                                                   push_dic
##        find_detail = find_dic.copy()
##        find_detail[key_level1+'.'+key_level2] = value_level2
##
##        push_dic_key = key_level1+'.$.'+update_dic.keys()[0]
##        push_dic_value = update_dic.values()[0]
##        push_dic = {push_dic_key : push_dic_value}
##
##        collect.update(find_detail, {'$push':push_dic}, False,False,False,True)
        
    #this function is to remove something new from records relating to some specific "corp_id" 
    def pullFromSet(self, collection, find_dic, del_dic):
        collect = self.db[collection]

        # add the record to one column
        collect.update(find_dic, {'$pull': del_dic})


##    def addToSet(self, collection, find_dic, set_dic):
##        collect = self.db[collection]
##
##        # add the record to one column
##        collect.update(find_dic, {'$addToSet': set_dic})

    #insert all records relating to a specific "corp_id" into mongoDB
    def insert(self,collection, new_record):
        collect = self.db[collection]

        collect.insert(new_record)
    
    def disconnect(self):
        self.conn.disconnect()
        
    def remove_all(self):
        for collection_name in self.collections:
            col = self.db[collection_name]
            col.remove({})
            
        self.disconnect()
        
class Test():
    def __init__(self):
        pass
    def test_insert(self):
        mon = Mongo('192.168.0.112',27017,'test')
        collection = 'han'
        mon.insert(collection, {'a': 1,
                                'b':2})
        
    def test_update(self):
        mon = Mongo('192.168.0.112',27017,'test')
        collection = 'han'
        find_dict = {'a':1}
        updated_dict = {'b':3}
        mon.update(collection, find_dict, updated_dict)
        
if __name__ == '__main__':
    from pprint import pprint
    from basic_functions import save_pickle
    if 0:
        mon = Mongo('192.168.0.112',27017,'test')
        collection = 'han'
        find_dic = {"comp_name" : "yahoo"}
        rm_record = {'corp_id':1}
        mon.unset(collection, find_dic, rm_record)
    
    if 0:
        test = Test()
        test.test_update()
        
    if 0:
        m = MongoEye(mongo_host='ec2-23-22-229-164.compute-1.amazonaws.com', 
                     mongo_database='monitor')
        
        for k, v in m.show_collections().iteritems():
            print k, v
            
        records = m.get_records('nlp_monitor', {})
        for r in records:
            record = r.items()
            break
        
        record.sort(key=lambda x: int(x[1]))
        
        pprint(record)
        
    if 0:
        m = MongoEye(mongo_host='ec2-23-22-229-164.compute-1.amazonaws.com', 
                     mongo_database='monitor')
        for k, v in m.show_collections().iteritems():
            print k, v
            
        for db in ['yixing','esdb','nlp']:
            records = m.get_records(db + '_monitor', {})
            for r in records:
                print r

    if 0:
        # 'company' db to test & retrieve competitors in 'crunchbase_company' collection
        m = MongoEye(mongo_host='ec2-23-22-229-164.compute-1.amazonaws.com', 
                 mongo_database='company')
        if 0:
            collections = m.show_collections()
            pprint(collections)

        #print m.show_all_possible_keys('crunchbase_info')
        #print m.show_all_possible_keys('description_info')
        #print m.show_all_possible_keys('crunchbase_company')

        output = []
        count = 1  
        for record in m.get_records('crunchbase_company', {}):
            #pprint(record.keys())
            competitions = record['competitions']
            if not competitions:
                #print "[INFO] No Competitors are Found!!!"
                continue
            competitors = [each['competitor']['name'] for each in competitions]
            competitors.append(record['name'])
            output.append(competitors)
            count += 1
            
            if not (count % 100): print "[INFO] # of competitor packages: %s" % count
            
            #pprint(competitors)
            #raw_input()

        save_pickle(output, 'rivals_in_crunchbase.pkl')

    if 0:
        m = MongoEye(mongo_host='ec2-23-22-229-164.compute-1.amazonaws.com', 
                 mongo_database='company_profile')
        output = {}
        for record in m.get_records('adwords_info', {}):
            domain = record.get('domain', None)
            adwords = record.get('adwords', None)
            
            if not (domain and adwords): continue
            
            output.setdefault(domain, [])
            output[domain].extend(adwords)
            
        save_pickle(output, "domain2adwords.pkl")
        
    if 1:
        m = MongoEye(mongo_host='ec2-23-22-229-164.compute-1.amazonaws.com', 
                 mongo_database='jinyi')
        with open("NLP_fund_raise_extracted_patterns_5_6_2013.txt", 'w') as wf:
            
            for i, record in enumerate(m.get_records('NLP_fund_raise_extracted_patterns_5_6_2013', {})):
                pattern = record.get('pattern', None)
                if not i % 50: print "[INFO] # of patterns: %s" % i 
                wf.write(pattern + '\n')
        
            
        
