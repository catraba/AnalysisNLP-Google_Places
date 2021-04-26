<script>
	import { Router, Route, Link } from 'svelte-navigator';
	import Demo from './components/Demo.svelte';

	let place_id;
	let promise = handleURL();

	async function handleURL (id) {
		/*
		This function get a place_id and make a request post
		to backend. Then it retrieves json response
		*/ 

		let response = await fetch('http://localhost:8000/test', {
									headers: {
										'Content-Type': 'application/json'
									},
									method: 'POST',
									body: JSON.stringify({'nombre': id})
							 });

		return response = await response.json();
	}

	function handleChange (id) {
		promise = handleURL(id);
	}

</script>

<!-- Define routes -->
<Router>
	<main>

		<Route path="/">
			<nav>
				<Link to="demo">Demo</Link>
			</nav>

			<div class="center">
				<h1 class="display-4">Análisis NLP con Google Places API</h1>

				<input bind:value={place_id} on:change={handleChange(place_id)} type="text" placeholder="Tip your Place ID" required>
				<a href="https://developers.google.com/maps/documentation/javascript/examples/places-placeid-finder" target="_blank">¿Place ID?</a>
			
				{#await promise}
					<p>Waiting...</p>
				{:then response}
					<div class="alert alert-danger" role="alert">
						{response['error_message']}
				  	</div>
				{/await}

			</div>
		</Route>


		<Route path="demo">
			<nav>
				<Link to="/">Atrás</Link>
			</nav>

			<Demo/>
		</Route>

	</main>
</Router>


<style>
	main {
		padding: 1em;
	}

	.center {
		padding: 320px 0;
		text-align: center;
	}

	.alert {	
		margin: auto;
		margin-top: 20px;
		width: 33%;
		padding: 10px;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>