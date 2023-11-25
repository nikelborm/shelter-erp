import { AntdEditInferencer } from "@refinedev/inferencer/antd";
import { GetServerSideProps } from "next";
import { authProvider } from "src/authProvider";

export default function AbstractPetEdit() {
  return <AntdEditInferencer hideCodeViewerInProduction />;
}

export const getServerSideProps: GetServerSideProps<{}> = async (context) => {
  const { authenticated, redirectTo } = await authProvider.check(context);

  if (!authenticated) {
    return {
      props: {},
      redirect: {
        destination: `${redirectTo}?to=${encodeURIComponent("/abstractPets")}`,
        permanent: false,
      },
    };
  }

  return {
    props: {},
  };
};
