{
    "services": [
        {
            "binary": "patron-scheduler",
            "host": "host1",
            "disabled_reason": "test1",
            "state": "up",
            "status": "disabled",
            "updated_at": "%(strtime)s",
            "zone": "internal"
        },
        {
            "binary": "patron-compute",
            "host": "host1",
            "disabled_reason": "test2",
            "state": "up",
            "status": "disabled",
            "updated_at": "%(strtime)s",
            "zone": "patron"
        },
        {
            "binary": "patron-scheduler",
            "host": "host2",
            "disabled_reason": null,
            "state": "down",
            "status": "enabled",
            "updated_at": "%(strtime)s",
            "zone": "internal"
        },
        {
            "binary": "patron-compute",
            "host": "host2",
            "disabled_reason": "test4",
            "state": "down",
            "status": "disabled",
            "updated_at": "%(strtime)s",
            "zone": "patron"
        }
    ]
}
