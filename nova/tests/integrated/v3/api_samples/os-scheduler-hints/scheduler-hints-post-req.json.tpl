{
    "server" : {
        "name" : "new-server-test",
        "imageRef" : "%(glance_host)s/openstack/images/%(image_id)s",
        "flavorRef" : "%(host)s/openstack/flavors/1",
        "os-scheduler-hints:scheduler_hints": {
            "same_host": "%(uuid)s"
        }
    }
}
