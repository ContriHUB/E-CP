import requests
import click

@click.command()
@click.argument('user',type=str)
def profile(user):
    try:
        response = requests.get(url='http://codeforces.com/api/user.info?handles='+user)
        if(response.status_code!=200):
            raise UsernameError('User not Found')
        html_content = response.json()
        print("*-*-*-*-*-*-**-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        print(
            "User Name : " + html_content["result"][0]["firstName"] + html_content["result"][0]["lastName"],
            "\nRating : " + str(html_content["result"][0]["rating"]),
            "\nContribution : " + str(html_content["result"][0]["contribution"]),
            "\nRank : " + str(html_content["result"][0]["rank"]),
            "\nMax Rating : " + str(html_content["result"][0]["maxRating"])
        )
        print("*-*-*-*-*-*-**-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
    except Exception() as e:
        click.echo(e)