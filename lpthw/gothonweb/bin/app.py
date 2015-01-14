
import web

web.config.debug = False

urls = (
    "/hello", "index",
    "/count", "count",
    "/reset", "reset"
)
app = web.application(urls, locals())
store = web.session.DiskStore("sessions")
session = web.session.Session(app, store, initializer={"count": 0})
render = web.template.render("templates/", base = "layout")


class index(object):

    def GET(self):
        return render.form()

    def POST(self):
        form = web.input(name = "Nobody", greeting = "Nothing")
        greeting = "%s, %s" % (form.greeting, form.name)

        return render.index(greeting = greeting)


class count(object):

    def GET(self):
        session.count += 1
        return str(session.count)


class reset(object):

    def GET(self):
        session.kill()
        return ""


if __name__ == "__main__":
    app.run()
