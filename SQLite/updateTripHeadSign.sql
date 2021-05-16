UPDATE trip as a set trip_headsign = (select stop_name from STOPS s, STOPSTIME s2 
where s2.trip_id = a.trip_id
and   s.stop_id = s2.stop_id
and   stop_sequence in(select max(stop_sequence) 
                       from STOPSTIME s3 
                       where s3.trip_id = s2.trip_id))