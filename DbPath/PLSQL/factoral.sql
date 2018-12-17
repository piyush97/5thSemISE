SET SERVEROUTPUT ON

DECLARE
	n NUMBER;
	i NUMBER;
    f NUMBER:=1;

BEGIN	
	FOR i IN 1..10 LOOP
			f := f * i;
		end loop;
	dbms_output.put_line(f);

END;
/
