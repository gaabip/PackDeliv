import { Empresa, Entregador, Veiculo, Endereco, Credenciais } from './../../interfaces/usuario';
import { Injectable } from '@angular/core';
import { Http, Headers, RequestOptionsArgs, Response } from '@angular/http';
import { Observable } from 'rxjs/Observable';

@Injectable()
export class UsuarioProvider {

  private url: string = 'http://localhost:5000/';

  constructor (public http: Http) {  }

  /**
   * getRequestOptions configura as opções das requisições.
   */
  private getRequestOptionsArgs(): RequestOptionsArgs {
    let headers = new Headers();
    headers.append('Content-Type', 'application/json');
    headers.append('X-Auth-Token', localStorage.getItem('token'));

    let options = {headers: headers};

    return options;
  }

  public fazerLogin(credenciais: Credenciais): Observable<any> {
    return this.http.post(this.url + 'login/', credenciais, this.getRequestOptionsArgs())
    .map((response: Response) => response.json());
  }

  public validarCNPJ(cnpj: string, callback: any): void {
    var resposta = {endereco: undefined, nome: undefined, cnpj: undefined};

    this.http.get(this.url + 'cnpj/' + cnpj)
    .map((response: Response) => response.json())
    .subscribe( response => {
      if (response.status != 'ERROR') {
        let cep = response.cep.replace('.', '').replace('-', '');
        let ender: Endereco = {
          street: response.logradouro,
          number: response.numero,
          complement: response.complemento,
          district: response.bairro,
          postal_code: cep,
          city: response.municipio,
          state: response.uf,
          country: 'BRASIL',
          type: response.tipo,
          lat: 0,
          long: 0
        };

        resposta.endereco = ender;
        resposta.nome = response.nome;
        resposta.cnpj = cnpj;

        callback(resposta);
      } else {
        console.log('Erro ao procurar pelo cnpj na base de dados da receitaws.');
        callback(false);
      }
    }, error => {
      console.log('Erro na validação de CNPJ: ' + error);
      callback(false);
    });
  }

  public cadastrarVeiculo(veiculo: Veiculo): Observable<any> {
    return this.http.post(this.url + 'vehicle/', veiculo, this.getRequestOptionsArgs())
    .map((response: Response) => response.json());
  }

  public cadastrarEmpresa(empresa: Empresa): Observable<any> {
    console.log(empresa);
    return this.http.post(this.url + 'company/', empresa, this.getRequestOptionsArgs())
      .map((response: Response) => response.json());
  }

  public cadastrarEntregador(entregador: Entregador): Observable<any> {
    return this.http.post(this.url+'deliveryman/', entregador, this.getRequestOptionsArgs())
    .map((response: Response) => response.json());
  }

  public atualizarPerfilEmpresa(usuario:Empresa, callback: any){
    this.http.put(this.url+'company/'+usuario.id, usuario, this.getRequestOptionsArgs())
    .subscribe( (res) => {
      alert('Perfil atualizado!');
      callback();
    }, (error) => {
      throw error;
    });
  }

  public atualizarPerfilEntregador(usuario:Empresa, callback: any){
    this.http.put(this.url+'deliveryman/'+usuario.id, usuario, this.getRequestOptionsArgs())
    .subscribe( (res) => {
      alert('Perfil atualizado!');
      callback();
    }, (error) => {
      throw error;
    });
  }

  public atualizarStatusEntregador(usuario:Empresa){
    this.http.put(this.url+'deliveryman/'+usuario.id, usuario, this.getRequestOptionsArgs())
    .subscribe( (res) => {
    }, (error) => {
      throw error;
    });
  }

}
