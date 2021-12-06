fetch("https://api.spotify.com/v1/me/player/currently-playing", {
    headers: {
        "Authorization": "Bearer BQDOgXT-TB3fueQlkN6snnMrj85UNDnKmJ7D9gWPQOQYCY_Mlnvs23wZxKGdzlUJl4V5cQmJI3_r8G3g6fztJrjuC1V8uTp_FRwjan5n2xGv8Qk4EAmyzLEk_zkysOl_qrxTX5VMWvRiRZ_D8X1CxzWp6jZpwuzbnN4YTyfj",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
})
    .then(response => response.json())
    .then(json => {
        console.log(json)
    })