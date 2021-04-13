export const loadedGoogleMapsAPI = new Promise( (resolve,reject) => {

  window['GoogleMapsInit'] = resolve;

  let GMap = document.createElement('script');

  GMap.setAttribute('src',
//  `https://maps.googleapis.com/maps/api/js?key=${process.env.GOOGLE_API_KEY}&callback=GoogleMapsInit&region=IN`);
`https://maps.googleapis.com/maps/api/js?key=AIzaSyB6SCXDq4PuAt-0PD3cV_DjZYwL1EyHwe0&callback=GoogleMapsInit&region=IN`);

  document.body.appendChild(GMap); 
});