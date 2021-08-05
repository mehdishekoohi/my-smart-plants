from flask import Flask, Response
from plivo import RestClient

app = Flask(__name__)


def send_sms():
    client = RestClient()
    message_created = client.messages.create(
        src='the_source_number',
        dst='the_destination_number',
        text='Hello, world!'
    )


@app.route('/send_sms/', methods=['GET', 'POST'])
def outbound_sms():
    client = RestClient('<auth_id>', '<auth_token>')
    response = client.messages.create(
      src='+14151234567',
      dst='+14157654321',
      text='Hello, from Flask!')
    return Response(response.to_string())


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
