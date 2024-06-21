

document.getElementById('businessForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting the traditional way

    // Get the value of the Business Name field
    const businessName = document.getElementById('businessName').value;
    const loc = document.getElementById('location').value;
    const date = document.getElementById('date').value;
    const data = {
        business:businessName,
        location:loc,
        date:date
    }
    console.log("Business Name:", businessName);
    console.log("Location:", loc);
    console.log("Date:", date);
    yelp_endPoint=`http://127.0.0.1:8000/`
    fetch("http://127.0.0.1:8000/",{
        method:'POST',
        body:JSON.stringify(data)
    })
    .then(response =>response.json())
    .then(data => {
        console.log("Success",data)
        incoming_data=document.getElementById("ClosestBusiness")
        incoming_data.innerText=data
        holiday_data={date:date}
        fetch("http://127.0.0.1:8000/Holiday/" , {
            method:'POST',
            body:JSON.stringify(holiday_data)
        })
        .then(response =>response.json())
        .then(data => {
            fetch("http://127.0.0.1:8000/DataBase/",{
                method:'POST',
                body:JSON.stringify(data)
            })
            .then(response => response.json())
            .then(data =>{
                statusHeader=document.getElementById("openStatus")
                statusHeader.innerText= data.status
            })


        })
        
       
    })
    // You can now use these values to make an API request or any other action
});
