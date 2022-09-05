from flask import render_template, request

from webserver_files.web_constants import WebMethod
import webserver_files.models as appmod
from webserver_files.settings import app, db

try:
    exec(open("database_config.py").read())
except:
    pass


@app.route("/", methods=[WebMethod.GET])
def home():
    return render_template("home.html")


@app.route("/create", methods=[WebMethod.GET, WebMethod.POST])
def create():
    if request.method == WebMethod.GET:
        return render_template("create.html")

    if request.method == WebMethod.POST:
        new_first_name = request.form["first_name"].capitalize()
        new_last_name = request.form["last_name"].capitalize()
        new_dob = request.form["DOB"]
        people = appmod.People.query.order_by(
            appmod.People.last_name, appmod.People.first_name
        ).all()

        for person in people:
            if (
                person.first_name == new_first_name
                and person.last_name == new_last_name
            ):
                exists = True
                return render_template("create.html", exists=exists)

        try:
            new_person = appmod.People(
                first_name=new_first_name, last_name=new_last_name, dob=new_dob
            )
            db.session.add(new_person)
            db.session.commit()
        except:
            dob_error = True
            return render_template("create.html", dob_error=dob_error)

        return render_template("home.html")


@app.route("/read", methods=[WebMethod.GET])
def read():
    people = appmod.People.query.order_by(
        appmod.People.last_name, appmod.People.first_name
    ).all()
    return render_template("read.html", people=people)


@app.route("/update", methods=[WebMethod.GET, WebMethod.POST])
def update():
    if request.method == WebMethod.GET:
        return render_template("update.html")

    if request.method == WebMethod.POST:
        prev_first_name = request.form["prev_first_name"].capitalize()
        prev_last_name = request.form["prev_last_name"].capitalize()
        updated_first_name = request.form["updated_first_name"].capitalize()
        updated_last_name = request.form["updated_last_name"].capitalize()
        updated_dob = request.form["updated_DOB"]
        people = appmod.People.query.order_by(
            appmod.People.last_name, appmod.People.first_name
        ).all()

        for person in people:
            if (
                person.first_name == prev_first_name
                and person.last_name == prev_last_name
            ):
                try:
                    updated_person = appmod.People(
                        first_name=updated_first_name,
                        last_name=updated_last_name,
                        dob=updated_dob,
                    )
                    db.session.add(updated_person)
                    db.session.delete(person)
                    db.session.commit()
                    return render_template("home.html")
                except:
                    dob_error = True
                    return render_template("update.html", dob_error=dob_error)

        not_exists = True
        return render_template("update.html", not_exists=not_exists)


@app.route("/delete", methods=[WebMethod.GET, WebMethod.POST])
def delete():
    if request.method == WebMethod.GET:
        return render_template("delete.html")

    if request.method == WebMethod.POST:
        first_name = request.form["first_name"].capitalize()
        last_name = request.form["last_name"].capitalize()
        people = appmod.People.query.order_by(
            appmod.People.last_name, appmod.People.first_name
        ).all()

        for person in people:
            if person.first_name == first_name and person.last_name == last_name:
                db.session.delete(person)
                db.session.commit()
                return render_template("home.html")

        not_exists = True
        return render_template("delete.html", not_exists=not_exists)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
