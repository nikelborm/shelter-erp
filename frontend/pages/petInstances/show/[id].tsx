import { AntdShowInferencer } from "@refinedev/inferencer/antd";
import { GetServerSideProps } from "next";
import { authProvider } from "src/authProvider";

// export default function PetInstanceShow() {
//   return <AntdShowInferencer />;
// }

import React from "react";
import { IResourceComponentsProps, useShow, useOne } from "@refinedev/core";
import {
    Show,
    DateField,
    TagField,
    TextField,
    NumberField,
} from "@refinedev/antd";
import { Typography } from "antd";

const { Title } = Typography;

const PetInstanceShow: React.FC<IResourceComponentsProps> = () => {
    const { queryResult } = useShow();
    const { data, isLoading } = queryResult;

    const record = data?.data;

    const { data: shelterData, isLoading: shelterIsLoading } = useOne({
        resource: "shelters",
        id: record?.shelterId || "",
        queryOptions: {
            enabled: !!record,
        },
    });

    const { data: abstractPetData, isLoading: abstractPetIsLoading } = useOne({
        resource: "abstractPets",
        id: record?.abstractPetId || "",
        queryOptions: {
            enabled: !!record,
        },
    });

    return (
        <Show isLoading={isLoading}>
            <Title level={5}>Shelter</Title>
            {shelterIsLoading ? (
                <>Loading...</>
            ) : (
                <>{shelterData?.data?.name}</>
            )}
            <Title level={5}>Animal class</Title>
            {abstractPetIsLoading ? (
                <>Loading...</>
            ) : (
                <>{JSON.stringify(abstractPetData?.data)}</>
            )}
            <Title level={5}>Was Brought At</Title>
            <DateField value={record?.wasBroughtAt} />
            <Title level={5}>Name</Title>
            <TextField value={record?.name} />
            <Title level={5}>Id</Title>
            <NumberField value={record?.id ?? ""} />
        </Show>
    );
};

export default PetInstanceShow;

export const getServerSideProps: GetServerSideProps<{}> = async (context) => {
  const { authenticated, redirectTo } = await authProvider.check(context);

  if (!authenticated) {
    return {
      props: {},
      redirect: {
        destination: `${redirectTo}?to=${encodeURIComponent("/petInstances")}`,
        permanent: false,
      },
    };
  }

  return {
    props: {},
  };
};
