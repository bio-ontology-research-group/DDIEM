@Grapes([
          @Grab(group='javax.servlet', module='javax.servlet-api', version='3.1.0'),
          @Grab(group='org.eclipse.jetty', module='jetty-server', version='9.4.8.v20171121'),
          @Grab(group='org.eclipse.jetty', module='jetty-servlet', version='9.4.8.v20171121'),
          @Grab(group='org.eclipse.jetty', module='jetty-servlets', version='9.4.8.v20171121'),
	  @GrabConfig(systemClassLoader=true)
	])
 
import org.eclipse.jetty.server.Server
import org.eclipse.jetty.server.ServerConnector
import org.eclipse.jetty.servlet.*
import groovy.servlet.*
import javax.servlet.*
import org.eclipse.jetty.servlets.*


//PORT = new Integer(args[0])
def startServer() {
  Server server = new Server(19000)

  def context = new ServletContextHandler(server, '/', ServletContextHandler.SESSIONS)

  context.resourceBase = '.'

  context.addServlet(GroovyServlet, '/autocomplete.groovy')
  context.addServlet(GroovyServlet, '/searchByID.groovy')
  context.addServlet(GroovyServlet, '/getTreatment.groovy')
  context.addServlet(GroovyServlet, '/getLinks.groovy')

  context.setAttribute('version', '0.1')

  FilterHolder cors = context.addFilter(CrossOriginFilter.class,"/*",EnumSet.of(DispatcherType.REQUEST))
  cors.setInitParameter(CrossOriginFilter.ALLOWED_ORIGINS_PARAM, "*")
  cors.setInitParameter(CrossOriginFilter.ACCESS_CONTROL_ALLOW_ORIGIN_HEADER, "*")
  cors.setInitParameter(CrossOriginFilter.ALLOWED_METHODS_PARAM, "GET,POST,HEAD")
  cors.setInitParameter(CrossOriginFilter.ALLOWED_HEADERS_PARAM, "X-Requested-With,Content-Type,Accept,Origin")


  server.start()
}

startServer()
