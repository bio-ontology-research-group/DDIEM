@Grab('mysql:mysql-connector-java:5.1.25')
@GrabConfig(systemClassLoader = true)
import groovy.sql.Sql
import java.sql.*
import groovy.json.*
if(!application) {
  application = request.getApplication(true)
}
def q = params.term
println new JsonBuilder(search(q))
def search(def q) {
    def url = 'jdbc:mysql://localhost:3306/DDIEM'
	def user = 'root'
	def driver = 'com.mysql.jdbc.Driver'
	def sql = Sql.newInstance(url, user,"", driver)
	def query=""
	if(q=="all"){
		query="SELECT name,id,OMIM_id FROM disease"		
	}
	else{
		query="SELECT name,id,OMIM_id FROM disease where name LIKE '"+q.toString()+"%' or OMIM_id LIKE '"+q.toString()+"%' limit 100"
	}
		List entities = sql.rows(query)
		sql.close()
    	return entities	
    
        
    }