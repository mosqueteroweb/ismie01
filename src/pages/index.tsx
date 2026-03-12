import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <Heading as="h1" className="hero__title">
          {siteConfig.title}
        </Heading>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/sirev/RA1_Teoria_rev">
            Empezar: Sistemas Informáticos ⏱️
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home(): JSX.Element {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Inicio | ${siteConfig.title}`}
      description="Portal educativo interactivo para ciclos formativos FP">
      <HomepageHeader />
      <main>
        <div className="container margin-top--lg padding-bottom--lg">
            <div className="row">
                <div className="col col--8 col--offset-2 text--center">
                    <h2>Bienvenido al Entorno de Aprendizaje Interactivo</h2>
                    <p>Este portal contiene la documentación teórica, prácticas de laboratorio y <b>bancos de evaluación interactivos</b> para el módulo de Sistemas Informáticos (SI) del ciclo DAM.</p>
                </div>
            </div>
            <div className="row margin-top--lg">
                <div className="col col--4">
                    <div className="card shadow--md">
                        <div className="card__header">
                            <h3>Teoría Profunda</h3>
                        </div>
                        <div className="card__body">
                            <p>Manuales enciclopédicos con diagramas de arquitectura para comprender el funcionamiento a bajo nivel de los sistemas.</p>
                        </div>
                    </div>
                </div>
                <div className="col col--4">
                    <div className="card shadow--md">
                        <div className="card__header">
                            <h3>Prácticas Reales</h3>
                        </div>
                        <div className="card__body">
                            <p>Casos prácticos de debugging, diseño de clases y administración de sistemas orientados a la realidad profesional.</p>
                        </div>
                    </div>
                </div>
                <div className="col col--4">
                    <div className="card shadow--md">
                        <div className="card__header">
                            <h3>Tests Interactivos</h3>
                        </div>
                        <div className="card__body">
                            <p>Ponte a prueba con los bancos de preguntas tipo test, obtén justificaciones exhaustivas de cada fallo y evalúa tu nivel.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
      </main>
    </Layout>
  );
}
