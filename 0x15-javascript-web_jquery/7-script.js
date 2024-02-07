const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
const div = $('div#character');
$.ajax({
  url: url,
  dataType: 'json'
}).done((data) => {
  div.text(data.name);
});
