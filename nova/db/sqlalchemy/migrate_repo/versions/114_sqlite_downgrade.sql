BEGIN TRANSACTION;
    CREATE TEMPORARY TABLE virtual_interfaces_backup (
        created_at DATETIME,
        updated_at DATETIME,
        deleted_at DATETIME,
        deleted BOOLEAN,
        id INTEGER NOT NULL,
        address VARCHAR(255),
	network_id INTEGER,
	instance_id INTEGER,
	instance_uuid VARCHAR(36),
	uuid VARCHAR(36),
        PRIMARY KEY (id)
    );

    INSERT INTO virtual_interfaces_backup
        SELECT created_at,
               updated_at,
               deleted_at,
               deleted,
               id,
	       address,
	       network_id,
               NULL,
	       instance_uuid,
	       uuid
        FROM virtual_interfaces;

    UPDATE virtual_interfaces_backup
        SET instance_id=
            (SELECT id
                 FROM instances
                 WHERE virtual_interfaces_backup.instance_uuid = instances.uuid
    );

    DROP TABLE virtual_interfaces;

    CREATE TABLE virtual_interfaces (
        created_at DATETIME,
        updated_at DATETIME,
        deleted_at DATETIME,
        deleted BOOLEAN,
        id INTEGER NOT NULL,
        address VARCHAR(255),
	network_id INTEGER,
	instance_id VARCHAR(36) NOT NULL,
	uuid VARCHAR(36),
        PRIMARY KEY (id),
        FOREIGN KEY(instance_id) REFERENCES instances (id)
    );

    CREATE INDEX virtual_interfaces_instance_id ON
    	virtual_interfaces(instance_id);
    CREATE INDEX virtual_interfaces_network_id ON
        virtual_interfaces(network_id);

    INSERT INTO virtual_interfaces
        SELECT created_at,
               updated_at,
               deleted_at,
               deleted,
               id,
               address,
	       network_id,
               instance_id,
	       uuid
        FROM virtual_interfaces_backup;

    DROP TABLE virtual_interfaces_backup;

COMMIT;