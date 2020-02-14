import asyncio


async def main(scope, receive, send):
    assert scope['type'] == 'http'

    qs = scope['query_string']

    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'Content-Type', b'text/html'],
        ]
    })

    await send({
        'type': 'http.response.body',
        'body': b'received path: ' + scope['raw_path'] + b'?' + qs
    })
