const contentContainer = document.getElementById('content-container')
const searchForm = document.getElementById('search-form')
const baseEndpoint = "http://localhost:8000/api"
if (searchForm) {
    // handle this login form
    searchForm.addEventListener('submit', handleSearch)
}

function handleSearch(event) {
    event.preventDefault()
    let formData = new FormData(searchForm)
    let data = Object.fromEntries(formData)
    let searchParams = new URLSearchParams(data)
    const endpoint = `${baseEndpoint}/search/?${searchParams}`
    const headers = {
        "Content-Type": "application/json",
    }
    const options = {
        method: "GET",
        headers: headers
    }
    fetch(endpoint, options) //  Promise
    .then(response=>{
        return response.json()
    })
    .then(data => {
        if (contentContainer){
            contentContainer.innerHTML = ""
            if (data && data.hits) {
                let htmlStr  = ""
                for (let result of data.hits) {
                    htmlStr += "<li>"+ result.title + "</li>"
                }
                contentContainer.innerHTML = htmlStr
                if (data.hits.length === 0) {
                    contentContainer.innerHTML = "<p>No results found</p>"
                }
            } else {
                contentContainer.innerHTML = "<p>No results found</p>"
            }
        }
    })
    .catch(err=> {
        console.log('err', err)
    })
}

const searchClient = algoliasearch('###', '###');

const search = instantsearch({
  indexName: '###',
  searchClient,
});

search.addWidgets([
  instantsearch.widgets.searchBox({
    container: '#searchbox',
  }),


  instantsearch.widgets.hits({
    container: '#hits',
    templates: {
      item(item) {
        return `<div>
        <div>Number: ${item._highlightResult.number.value}</div>
        <div>Cities: ${item._highlightResult.city_names
          .map(({ value }) => `${value}`)
          .join(', ')}</div>
      </div>`;
      },
    },
  })
]);

search.start();
