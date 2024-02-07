const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
const movies = $('ul#list_movies');
$.ajax({
    url: url,
    dataType: 'json'
}).done((data) => {
    const list = data.results;
    for (let i = 0; i < movies.length; ++i) {
        const title = movies[i].title;
        const elem = `<li>${title}`;
        movies.append(element);
    }
});