import { ProblemaEnum } from "../enums/problema.enum";

export class ParametrosEjercicioDTO{
    public problema! : ProblemaEnum;
    public algoritmo! : string;
    public requerimientos! : any;

    constructor(){}
}