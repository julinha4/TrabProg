$(document).ready(function () {

    $("#link_listar_novelas").click(function () {
        $.ajax({
            url: 'http://localhost:5000/listar_novelas',
            method: 'GET',
            dataType: 'json',
            success: listar_novelas,
            error: function () {
                alert("erro ao ler dados, verifique o backend");
            }
        });
        function listar_novelas(novelas) {
            $('#corpoTabelaNovelas').empty();
            for (var i in novelas) {
                lin = '<tr id="linha_'+novelas[i].id+'">' +
                    '<td>' + novelas[i].nome +
                    '<td>' + novelas[i].emissora +
                    '<td style="width:250px">'+ novelas[i].data_transmissao +
                    '<td>' + novelas[i].genero.tipo +
                    '<td>' + novelas[i].genero.popularidade +
                    '<td><a href=# id="excluir_' + novelas[i].id + '" ' +
                    'class="excluir_novela"><img height="50px" src="img/excluir.png" ' +
                    'alt="Excluir novela" title="Excluir novela"></a>'
                '<tr>';
                $('#corpoTabelaNovelas').append(lin);
            }
        }
        });

        $("#btn_inc_novela").click(function(){
            nome_novela = $("#nome_novela").val();
            emissora = $("#emissora").val();
            data_transmissao = $("#data_transmissao").val();
            genero_id = $("#genero_id").find('option:selected').attr("name");
            dados = JSON.stringify({nome : nome_novela, emissora : emissora, data_transmissao : data_transmissao, genero_id : genero_id});
            $.ajax({
              url:'http://localhost:5000/incluir_novela',
              type: 'POST',
              contentType: 'application/json',
              dataType: 'json',
              data: dados,
              success: incluirNovela,
              error: function(){
                  alert("deu erro")
              }
            });

            function incluirNovela(resposta){
              if (resposta.resultado == "ok"){
                alert("Novela incluida com sucesso, obrigado!");
                $("#nome_novela").val("");
                $("#emissora").val("");
                $("#data_transmissao").val("");
              } else {
                alert("Deu ruim!");
              }
            }
          })

        $("#link_listar_personagens").click(function() {
            $.ajax({
              url: 'http://localhost:5000/listar_personagens',
              method: 'GET',
              dataType: 'json',
              success: listar_personagens, 
              error: function() {
                  alert("erro ao ler dados, verifique o backend");
              }
          });
              function listar_personagens (personagens) {
                $('#corpoTabelaPersonagens').empty();
                for (var i in personagens) { 
                    lin = '<tr id="linha_'+personagens[i].id+'">' +
                    '<td style="width:250px">' + personagens[i].nome + '</td>' + 
                    '<td style="width:250px">' + personagens[i].idade + '</td>' + 
                    '<td style="width:200px">' + personagens[i].resumo + '</td>' +
                    '<td> <a href=# id="excluir_' + personagens[i].id + '" ' +
                          'class="excluir_personagem"><img style="widht:30px; height:50px;" src="img/excluir.png" '+
                          'alt="Excluir personagem" title="Excluir personagem"></a>' + 
                        '</td>' + 
                    '</tr>';
                    $('#corpoTabelaPersonagens').append(lin);
            }}
        });

        $(document).on("click", ".excluir_novela", function() {
            var componente_clicado = $(this).attr('id');  
            var nome_icone = "excluir_";
            var id_novela = componente_clicado.substring(nome_icone.length);

            $.ajax({
                url: 'http://localhost:5000/excluir_novela/'+id_novela,
                type: 'DELETE', 
                dataType: 'json', 
                success: novelaExcluida, 
                error: function(){
                    alert("deu erro")
                }
            });
            function novelaExcluida(retorno) {
                if (retorno.resultado == "ok") { 
                    $("#linha_" + id_novela).fadeOut(1000, function(){
                        alert("Novela excluida com sucesso!");
                    });
                } else {
                    alert(retorno.resultado + ":" + retorno.detalhes);
                }            
            }

        });
    

        

        

});


