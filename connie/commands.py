import click
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

# Necessary permits and access to the file
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
cred_path = r"C:\Users\danie\PycharmProjects\connie\connie-423215-4dfbde934222.json"
credentials = ServiceAccountCredentials.from_json_keyfile_name(cred_path, scope)
gc = gspread.authorize(credentials)
spreadsheet_id = "1u7A8cQg5bcJ5wD1mOqMBee_f2bpEruFX0RKACVoVwuM"
sheet_name = "Foglio1"
worksheet = gc.open_by_key(spreadsheet_id).worksheet(sheet_name)
data = worksheet.get_all_records()
df = pd.DataFrame(data)


@click.command("add", help="Add a row of data to the work_net DataFrame")
def add():
    """"""
    int_type = click.prompt("Which type of interaction you want to add?", type=click.Choice(["req_pos", "adm"]))
    if int_type.lower() == "adm":
        object = click.prompt("Which is the object of the interaction?")
    else:
        object = ""
    req_type = click.prompt("Are you applying for a position or asking for it?",
                            type=click.Choice(["asking", "applying"]))
    pos_type = click.prompt("What kind of position are you interested in?",
                            type=click.Choice(["industry", "intern", "PhD"]))
    deadline = ""
    if req_type.lower() == "applying":
        if click.confirm("There is a deadline?"):
            deadline = click.prompt("When is the deadline", type=click.DateTime(formats=["%d-%m-%Y"]))
    status = click.prompt("Which is the status of the interaction?", type=click.Choice(["p", "wtr", "wmr", "closed"]))
    qual1, qual2 = "", ""
    if click.confirm("There is a reference person?"):
        name = click.prompt("Which is the name of the person you're interacting with?")
        surname = click.prompt("Which is the surname of the person you're interacting with?")
        if click.confirm("The person you're interacting with is a Prof.?"):
            qual1 = "Prof."
        else:
            qual1 = ""
        if click.confirm("The person you're interacting with is a Dr.?"):
            qual2 = "Dr."
        else:
            qual2 = ""
    else:
        name, surname = "", ""
    if click.confirm("There is a reference email?"):
        email = click.prompt("Which is the email of the person you're interacting with?")
    else:
        email = ""
    institution = click.prompt("Which institution/industry you're interacting with?")
    city = click.prompt("In which city the person/institution is located?")
    if click.confirm("Are you asking to take part to a project?"):
        project = click.prompt("Which is the name of the project?")
    else:
        project = ""

    new_row = {'int_type': int_type, 'req_type': req_type, "pos_type": pos_type, 'deadline': deadline,
               "status": status, "qual1": qual1, "qual2": qual2, "name": name, "surname": surname,
               "institution": institution, "city": city, "project": project, "object": object, "email": email}
    df.loc[len(df.index)] = new_row
    # print(df)

    try:
        worksheet.update([df.columns.values.tolist()] + df.values.tolist())
        print("The Google Sheet document was updated successfully :)")
    except Exception as e:
        print("An error has occurred during the update of the Google Sheet document:", e)


@click.command("add", help="Add a row of data to the work_net DataFrame")
def delete():
    index_to_drop = df[df['B'] == 'z'].index
    df.drop(index_to_drop)

@click.command("clear_closed", help="Remove all the closed interactions from the DataFrame")
def clear_closed():
    grouped_indices = df.groupby("status").groups
    closed = grouped_indices.get("closed", [])

