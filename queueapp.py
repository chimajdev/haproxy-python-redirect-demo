import asyncio

WAITSECS = 3


async def main(scope, receive, send):
    assert scope['type'] == 'http'

    # waiting
    await asyncio.sleep(WAITSECS)

    # preparing updated query string
    qs = scope['query_string']
    if qs != b'':
        qs += b'&'
    qs += b'appTalk=redirectFromSleep'

    # sending response with location header
    await send({
        'type': 'http.response.start',
        'status': 302,
        'headers': [
            [b'Location', scope['raw_path'] + b"?" + qs],
        ]
    })

    await send({
        'type': 'http.response.body',
    })
