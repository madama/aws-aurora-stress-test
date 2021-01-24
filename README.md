[![Build Status](https://travis-ci.com/madama/aws-aurora-stress-test.svg?branch=master)](https://travis-ci.com/madama/aws-aurora-stress-test)

# AWS Aurora Stress Test

## MySQL
Create the table
```
CREATE TABLE iterations (
  id char(40) PRIMARY KEY,
  timestamp INT NOT NULL
);
```

Here the stored procedure to consume resources

```
DELIMITER $$

CREATE PROCEDURE eat_cpu(IN cycles INT)
BEGIN
  declare `start` int;
  set start = 0;

  WHILE start < cycles DO
    INSERT INTO iterations VALUES(UUID(), UNIX_TIMESTAMP(NOW()));
    Set start = start + 1;
  END WHILE;
  SELECT COUNT(*) FROM iterations;
END;

$$

DELIMITER ;
```
