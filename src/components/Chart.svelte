<script>
    import Chart from 'chart.js';
    import { onMount } from 'svelte';


    async function createChart() {

        let response = await fetch('http://localhost:8000/demo');
		response = await response.json();

        // Gráfica cantidad de puntuaciones por nota

        var punt_list = new Array;

        for (const property in response.cantidad_puntuaciones) {
            punt_list.push(response.cantidad_puntuaciones[property])
        };

        console.log(punt_list);

        var ctx = document.getElementById('valoraciones_por_nota').getContext('2d');
        var graphic_bar = new Chart(ctx, {

            type: 'bar',
            data: {
                labels: [1, 2, 3, 4, 5],
                datasets: [{
                    data: punt_list,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)'
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                legend: false,
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }
        });


        // Gráfica media de puntuaciones por año

        var ages = new Array;
        var punt_age_list = new Array;

        for (const property in response.reviews_by_year) {
            ages.push(property)
            punt_age_list.push(response.reviews_by_year[property])
        };

        var ctx = document.getElementById('media_por_año').getContext('2d');
        var graphic_line = new Chart(ctx, {
            type: 'line',
            data: {
                labels: ages,
                datasets: [{
                    data: punt_age_list
                }]
            },
            options: {
                legend: false
            }
        });
    };   

    onMount(createChart);

</script>


<div class="parent flex-parent">
    <div class="child flex-child">
        <canvas id="valoraciones_por_nota"></canvas>
    </div>
    <div class="child flex-child">
        <canvas id="media_por_año"></canvas>
    </div>
</div>


<style>
    /*.chart-container {
        position: relative;
        height: 40vh;
        width: 40vw;
    }*/
    .flex-parent {
        display: flex;
    }
    .flex-child {
        flex: 1;
    }
</style>