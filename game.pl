#!/usr/bin/perl -W
use IO::Socket;
srand;
my $sleep_len = rand()*600;
print "Sleeping for: " . $sleep_len. "\n";
print "";

sleep($sleep_len);

my $sock = IO::Socket::INET->new(PeerAddr=>'api.foursquare.com', PeerPort=>80, 
                                 Proto =>'tcp', Type=>SOCK_STREAM) or die;
$ARGV[1] += rand() * 0.0001 - 0.00005;
$ARGV[2] += rand() * 0.0001 - 0.00005;
my $str = "vid=$ARGV[0]&private=0&geolat=$ARGV[1]&geolong=$ARGV[2]";
print $sock "POST /v1/checkin HTTP/1.1\r\nHost: api.foursquare.com\r\nUser-Agent:"
            ." Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en) AppleWebKit/420+ "
            ."(KHTML, like Gecko) Version/3.0 Mobile/1C10 Safari/419.3\r\nContent"
            ."-Type: application/x-www-form-urlencoded\r\nAuthorization: Basic "
            ."[YOUR BASE64 CREDENTIALS HERE]\r\nContent-length: ", length($str)+2, "\r\n\r\n$str\r\n";
$_=<$sock>;  
