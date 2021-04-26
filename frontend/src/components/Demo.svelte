<script>
    import Chart from 'chart.js';
    import { onMount } from 'svelte';


    async function createChart() {

        // Gráfica cantidad de puntuaciones

        var ctx = document.getElementById('valoraciones_por_nota').getContext('2d');
        var graphic_bar = new Chart(ctx, {

            type: 'bar',
            data: {
                labels: [1, 2, 3, 4, 5],
                datasets: [{
                    data: [45, 22, 26, 57, 77],
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)'
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

        var ctx = document.getElementById('media_por_año').getContext('2d');
        var graphic_line = new Chart(ctx, {
            type: 'line',
            data: {
                labels: [2014, 2015, 2016, 2017, 2018, 2019, 2020],
                datasets: [{
                    data: [3.1, 3.9, 3.3, 4.1, 3.2, 2.5, 2.8],
                    borderColor: 'rgba(75, 192, 192)',
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


        // Gráfica de adjetivos más repetidos

        var ctx = document.getElementById('adjetivos').getContext('2d');
        var graphic_pie = new Chart(ctx, {
            type: 'pie',
            data: {
                labels: ['atento', 'pesimo', 'excelente', 'amable', 'impecable', 'agradable', 'deficiente', 'lento', 'malo', 'encantador'],
                datasets: [{
                    data: [5, 3, 2, 2, 2, 1, 1, 1, 1, 1],
                    backgroundColor: [
                        'rgb(255, 99, 132)',
                        'rgb(54, 162, 235)',
                        'rgb(255, 205, 86)',
                        'rgb(75, 192, 192)',
                        'rgb(153, 102, 255)',
                        'rgb(255, 171, 14)',
                        'rgb(248, 87, 241)',
                        'rgb(178, 229, 83)',
                        'rgb(98, 94, 234)',
                        'rgb(198, 170, 158)'
                    ],
                    hoverOffset: 4
                }]
            },
            options: {
                legend: {
                    position: 'right',
                }
            }
        });

    };   

    onMount(createChart);

</script>



<div class="row">
    <h1 class="display-1">Trocadero Sotogrande</h1>
    <p><small>1108 reviews / 4.3 average rating</small></p>
</div>


<div class="row">
    <div class="col-sm-6">
        <div class="card">
            <div class="card-body">
                <p class="lead">Title 1</p>
                <canvas id="valoraciones_por_nota"></canvas>
            </div>
        </div>
    </div>
    <div class="col-sm-6">
        <div class="card">
            <div class="card-body">
                <p class="lead">Title 2</p>
                <canvas id="media_por_año"></canvas>
            </div>
        </div>
    </div>
</div>


<div class="row">
    <div class="col-sm-3">
        <div class="card">
            <div class="card-body">
              <p class="lead">Top used words</p>
                <ol class="list-group list-group-numbered">
                    <li class="list-group-item d-flex justify-content-between align-items-start">
                      <div class="ms-2 me-auto">
                        sitio
                      </div>
                      <span class="badge bg-primary rounded-pill">82</span>
                    </li>
                    <li class="list-group-item d-flex justify-content-between align-items-start">
                      <div class="ms-2 me-auto">
                        cena
                      </div>
                      <span class="badge bg-primary rounded-pill">59</span>
                    </li>
                    <li class="list-group-item d-flex justify-content-between align-items-start">
                      <div class="ms-2 me-auto">
                        bonito
                      </div>
                      <span class="badge bg-primary rounded-pill">57</span>
                    </li>
                    <li class="list-group-item d-flex justify-content-between align-items-start">
                        <div class="ms-2 me-auto">
                        servicio
                        </div>
                        <span class="badge bg-primary rounded-pill">41</span>
                      </li>
                      <li class="list-group-item d-flex justify-content-between align-items-start">
                        <div class="ms-2 me-auto">
                        lamentable
                        </div>
                        <span class="badge bg-primary rounded-pill">38</span>
                      </li>
                      <li class="list-group-item d-flex justify-content-between align-items-start">
                        <div class="ms-2 me-auto">
                        desastre
                        </div>
                        <span class="badge bg-primary rounded-pill">34</span>
                      </li>
                      <li class="list-group-item d-flex justify-content-between align-items-start">
                        <div class="ms-2 me-auto">
                          lujo
                        </div>
                        <span class="badge bg-primary rounded-pill">32</span>
                      </li>
                      <li class="list-group-item d-flex justify-content-between align-items-start">
                        <div class="ms-2 me-auto">
                          comida
                        </div>
                        <span class="badge bg-primary rounded-pill">30</span>
                      </li>
                      <li class="list-group-item d-flex justify-content-between align-items-start">
                        <div class="ms-2 me-auto">
                          impresionante
                        </div>
                        <span class="badge bg-primary rounded-pill">27</span>
                      </li>
                      <li class="list-group-item d-flex justify-content-between align-items-start">
                        <div class="ms-2 me-auto">
                          restaurante
                        </div>
                        <span class="badge bg-primary rounded-pill">21</span>
                      </li>
                      <li class="list-group-item d-flex justify-content-between align-items-start">
                        <div class="ms-2 me-auto">
                          playa
                        </div>
                        <span class="badge bg-primary rounded-pill">19</span>
                      </li>
                      <li class="list-group-item d-flex justify-content-between align-items-start">
                        <div class="ms-2 me-auto">
                          perfecto
                        </div>
                        <span class="badge bg-primary rounded-pill">13</span>
                      </li>
                      <li class="list-group-item d-flex justify-content-between align-items-start">
                        <div class="ms-2 me-auto">
                          decepcionante
                        </div>
                        <span class="badge bg-primary rounded-pill">8</span>
                      </li>
                      <li class="list-group-item d-flex justify-content-between align-items-start">
                        <div class="ms-2 me-auto">
                          trocadero
                        </div>
                        <span class="badge bg-primary rounded-pill">7</span>
                      </li>
                      <li class="list-group-item d-flex justify-content-between align-items-start">
                        <div class="ms-2 me-auto">
                          visita
                        </div>
                        <span class="badge bg-primary rounded-pill">3</span>
                      </li>

                  </ol>
            </div>
        </div>
    </div>
    <div class="col-sm-9">
        <div class="card">
            <div class="card-body">
                <p class="lead">Title 3</p>
                <div class="row">
                    <div class="col-sm-2">
                        <label for="adj" class="form-label"></label>
                        <input type="text" class="form-control" id="adj" placeholder="Ej: 'servicio'">

                        <select class="form-select">
                            <option>All</option>
                            <option>2014</option>
                            <option>2015</option>
                            <option>2016</option>
                            <option>2017</option>
                            <option>2018</option>
                            <option>2019</option>
                            <option>2020</option>
                        </select>

                        <button type="button" class="btn btn-outline-success">Success</button>
                    
                        <div class="card text-dark bg-light mb-3" style="bottom: -150px">
                          <div class="card-header">Rating</div>
                          <div class="card-body">
                            <h1 class="display-1">3.05</h1>
                          </div>
                        </div>
                    </div>
                    <div class="col-sm-10">
                        <canvas id="adjetivos"></canvas>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>


<style>
    .row {
      margin: auto;
      margin-top: 20px;
    }

    select {
      margin-top: 10px;
    }

    button {
      margin-top: 10px;
      width: 100%;
    }
</style>