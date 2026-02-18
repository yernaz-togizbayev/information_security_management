To solve this challenge I referred to this website "https://pentest-tools.com/blog/sql-injection-attacks". It gave me ideas how typical sql injection look like.
For the first time, I just opened the website and logged in with provided cre4dentials, just to see what this web application contains. At second time I tried
to log in with access ID "' OR '1'='1" to see, if it can be hacked already at the loggin page. For password I entered just anything. Unfortunately I couldn't
access the website. Then I opened DevTools and tried to change the value of access ID form to "' OR '1'='1" and log in with this, but no success either. So after
some several times of trying, I gave up and just entered the website again with provided credentials. And there I saw an form with access ID which I just entered
and tried to rework it. So I changed its value to "' OR '1'='1" again and pressed "Request information". And this time, instead of showing me bank information of
"Jack Black", it showed me a bank data for "Fernando Swarm Worm Gonzales" and here I could collect information of his debt. Now, since I know that "form" part of
website suffers under SQL injection and I tried some other queries. This time I used 'UNION'. So I replaced the whole form line with

	<input type="hidden" value="' UNION SELECT * FROM credit OFFSET 2 --" name="access">
	
and this showed me bank data for "Fransen Mobitu", and so I could collect his credit card number. As next, I just kept increasing OFFSET number until I find all
necessary information.

As last, I entered 'Request Information' and found there a script part with secret.jpg. As I could refer to a challenge hint, we could use uudecode. So I copied
the contect of this script into some text file, e.g. "secret_image.txt", and then executed "uudecode secret_image.txt", which then gave me an output "secret.jpg".
So I opened this picture, but didn't realize at first, what this picture is about. After some time, I noticed a tiny yellow text at the bottom of picture.